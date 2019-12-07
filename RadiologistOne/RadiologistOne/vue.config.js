const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  devServer: {
    proxy: "http://localhost:3000",
    port: 3000
  },
  configureWebpack: {
    plugins: [
      // copy decoders
      new CopyWebpackPlugin([
        {
          from: "./node_modules/dwv/decoders",
          to: "assets/dwv/decoders"
        }
      ])
    ]
  },
  outputDir: "build"
};
