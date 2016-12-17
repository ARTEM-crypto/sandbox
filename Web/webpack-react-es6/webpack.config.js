var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: './app/javascript/main.js',
    output: { path: __dirname + '/bin', filename: 'bundle.js' },
    module: {
        loaders: [
            {
                test: /.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    },
};