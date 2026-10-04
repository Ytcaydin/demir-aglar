package com.ytcaydin.demiraglar;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.VibrationEffect;
import android.os.Vibrator;
import android.util.Base64;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

import androidx.core.content.FileProvider;
import androidx.webkit.WebViewAssetLoader;

import org.json.JSONArray;

import java.io.File;
import java.io.FileOutputStream;

/**
 * Demir Ağlar: oyunun HTML sürümünü uygulamanın içinden, internetsiz açan kabuk.
 * Dosyalar assets/www altından https://appassets.androidplatform.net adresiyle sunulur,
 * böylece kayıtlar (localStorage) kalıcı olur ve sayfa güvenli bağlamda çalışır.
 */
public class MainActivity extends Activity {
    private static final String HOST = "appassets.androidplatform.net";
    private static final String START = "https://" + HOST + "/assets/www/index.html";

    private WebView web;
    private WebViewAssetLoader loader;
    private boolean immersive = false;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);

        FrameLayout root = new FrameLayout(this);
        root.setBackgroundColor(Color.parseColor("#10202A"));
        web = new WebView(this);
        web.setBackgroundColor(Color.parseColor("#10202A"));
        root.addView(web, new FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT));
        setContentView(root);

        // Android 15 uygulamayı kenardan kenara çizer: içeriği durum ve gezinme çubuklarının dışında tut.
        root.setOnApplyWindowInsetsListener((v, insets) -> {
            int l, t, r, b;
            if (Build.VERSION.SDK_INT >= 30) {
                android.graphics.Insets i = insets.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout());
                l = i.left; t = i.top; r = i.right; b = i.bottom;
            } else {
                l = insets.getSystemWindowInsetLeft(); t = insets.getSystemWindowInsetTop();
                r = insets.getSystemWindowInsetRight(); b = insets.getSystemWindowInsetBottom();
            }
            v.setPadding(l, t, r, b);
            return insets;
        });

        loader = new WebViewAssetLoader.Builder()
                .setDomain(HOST)
                .addPathHandler("/assets/", new WebViewAssetLoader.AssetsPathHandler(this))
                .build();

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setTextZoom(100);
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);
        s.setSupportZoom(false);
        s.setBuiltInZoomControls(false);

        web.addJavascriptInterface(new Bridge(), "AndroidBridge");
        web.setWebChromeClient(new WebChromeClient());
        web.setWebViewClient(new WebViewClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest req) {
                return loader.shouldInterceptRequest(req.getUrl());
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest req) {
                Uri u = req.getUrl();
                if (HOST.equals(u.getHost())) return false;
                // Oyunun dışındaki bağlantılar tarayıcıda açılsın.
                try {
                    startActivity(new Intent(Intent.ACTION_VIEW, u));
                } catch (ActivityNotFoundException e) {
                    // açacak uygulama yok
                }
                return true;
            }
        });

        if (state != null) web.restoreState(state);
        else web.loadUrl(START);
    }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    protected void onPause() {
        // Uygulama arka plana geçerken oyunu kaydet.
        web.evaluateJavascript("try{persist()}catch(e){}", null);
        web.onPause();
        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        web.onResume();
    }

    @Override
    protected void onDestroy() {
        if (web != null) {
            web.destroy();
            web = null;
        }
        super.onDestroy();
    }

    @Override
    @SuppressWarnings("deprecation")
    public void onBackPressed() {
        if (web == null) {
            moveTaskToBack(true);
            return;
        }
        // Önce oyun kendi katmanlarını kapatsın (tam ekran menüsü, fotoğraf modu); kapatacak bir şey yoksa uygulamayı arka plana al.
        web.evaluateJavascript("(window.fsBack&&fsBack())?'1':'0'", v -> {
            if ("\"1\"".equals(v)) return;
            if (web != null && web.canGoBack()) web.goBack();
            else moveTaskToBack(true);
        });
    }

    @SuppressWarnings("deprecation")
    private void applyImmersive(boolean on) {
        immersive = on;
        View d = getWindow().getDecorView();
        if (Build.VERSION.SDK_INT >= 30) {
            WindowInsetsController c = d.getWindowInsetsController();
            if (c == null) return;
            if (on) {
                c.hide(WindowInsets.Type.systemBars());
                c.setSystemBarsBehavior(WindowInsetsController.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);
            } else {
                c.show(WindowInsets.Type.systemBars());
            }
        } else {
            d.setSystemUiVisibility(on
                    ? View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY | View.SYSTEM_UI_FLAG_FULLSCREEN | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                    | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                    : View.SYSTEM_UI_FLAG_VISIBLE);
        }
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        // Bildirim panelinden dönünce çubuklar yeniden gizlensin.
        if (hasFocus && immersive) applyImmersive(true);
    }

    /** Sayfanın çağırdığı yerel işlevler: paylaşım sayfası, titreşim ve tam ekran. */
    private class Bridge {
        @JavascriptInterface
        public void setImmersive(boolean on) {
            runOnUiThread(() -> applyImmersive(on));
        }

        @JavascriptInterface
        public void shareImage(String base64Png, String text) {
            try {
                byte[] png = Base64.decode(base64Png, Base64.DEFAULT);
                File dir = new File(getCacheDir(), "share");
                if (!dir.exists() && !dir.mkdirs()) return;
                File f = new File(dir, "demir-aglar.png");
                try (FileOutputStream o = new FileOutputStream(f)) {
                    o.write(png);
                }
                Uri uri = FileProvider.getUriForFile(MainActivity.this, getPackageName() + ".fileprovider", f);
                Intent send = new Intent(Intent.ACTION_SEND);
                send.setType("image/png");
                send.putExtra(Intent.EXTRA_STREAM, uri);
                if (text != null && !text.isEmpty()) send.putExtra(Intent.EXTRA_TEXT, text);
                send.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                Intent chooser = Intent.createChooser(send, getString(R.string.share_title));
                runOnUiThread(() -> {
                    try {
                        startActivity(chooser);
                    } catch (ActivityNotFoundException e) {
                        // paylaşacak uygulama yok
                    }
                });
            } catch (Exception e) {
                // paylaşım başarısız: oyun etkilenmesin
            }
        }

        @JavascriptInterface
        @SuppressWarnings("deprecation")
        public void vibrate(String pattern) {
            try {
                Vibrator v = (Vibrator) getSystemService(VIBRATOR_SERVICE);
                if (v == null || !v.hasVibrator()) return;
                String p = pattern == null ? "" : pattern.trim();
                if (p.startsWith("[")) {
                    JSONArray a = new JSONArray(p);
                    if (a.length() == 0) return;
                    long[] w = new long[a.length() + 1];
                    w[0] = 0;
                    for (int i = 0; i < a.length(); i++) w[i + 1] = Math.max(0, a.optLong(i));
                    if (Build.VERSION.SDK_INT >= 26) v.vibrate(VibrationEffect.createWaveform(w, -1));
                    else v.vibrate(w, -1);
                } else {
                    long ms = Math.max(1, Math.min(2000, (long) Double.parseDouble(p)));
                    if (Build.VERSION.SDK_INT >= 26) v.vibrate(VibrationEffect.createOneShot(ms, VibrationEffect.DEFAULT_AMPLITUDE));
                    else v.vibrate(ms);
                }
            } catch (Exception e) {
                // titreşim yoksa sessizce geç
            }
        }
    }
}
