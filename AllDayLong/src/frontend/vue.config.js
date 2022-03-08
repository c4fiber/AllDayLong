const path = require('path')
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    outputDir: path.resolve(__dirname, "../" + "main/resources/static"),
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8081',
                ws: true,
                changeOrigin: true
            }
        }
    },
    transpileDependencies: true
})
