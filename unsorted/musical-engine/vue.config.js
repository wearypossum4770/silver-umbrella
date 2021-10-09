module.exports = {

  lintOnSave: false,
  crossorigin: "anonymous",
  devServer: {
    host: '0.0.0.0',
    hot: true,
    disableHostCheck: true,
  },
  pluginOptions: {
    apollo: { lintGQ: true },
    pwa: {
      name: "My App",
      themeColor: "#4DBA87",
      msTileColor: "#000000",
      appleMobileWebAppCapable: "yes",
      appleMobileWebAppStatusBarStyle: "black",
      // configure the workbox plugin
      workboxPluginMode: "InjectManifest",
      workboxOptions: {
        // swSrc is required in InjectManifest mode.
        swSrc: "dev/sw.js", // ...other Workbox options...
      },
    },
    i18n: {
      locale: undefined,
      fallbackLocale: undefined,
      localeDir: undefined,
      enableInSFC: undefined,
    },
  },
};
