const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],

  outputDir: 'dist',
  publicPath: '/',
  assetsDir: 'static',
})
