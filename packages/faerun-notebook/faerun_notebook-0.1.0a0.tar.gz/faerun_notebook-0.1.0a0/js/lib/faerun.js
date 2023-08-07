var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
var TMAP = require('tmap-faerun-js');

require('./faerun.css');

// See *.js.py for the kernel counterpart to this file.


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var FaerunModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name: 'FaerunModel',
        _view_name: 'FaerunView',
        _model_module: 'faerun-notebook',
        _view_module: 'faerun-notebook',
        _model_module_version: '0.1.0',
        _view_module_version: '0.1.0',
        x: [],
        y: [],
        z: [],
        c: [],
        cmap: 'viridis',
        width: 400,
        height: 400,
        color: '#000000',
        background_color: '#ffffff',
        view: 'free',
        full_width: false,
        hovered_index: -1,
        selected_index: -1
    })
});


// Custom View. Renders the widget model.
var FaerunView = widgets.DOMWidgetView.extend({
    // Defines how the widget gets rendered into the DOM
    render: function () {
        this._faerunContainer = document.createElement('div');
        this._faerunHoverIndicator = document.createElement('div');
        this._faerunCanvas = document.createElement('canvas');
        this._faerunContainer.setAttribute('style', 'position: relative');
        this._faerunCanvas.setAttribute('id', 'faerun-canvas');

        if (this.model.get('full_width')) {
            this._faerunCanvas.setAttribute('style', `width:100%; height:${this.model.get('height')}px`);
        } else {
            this._faerunCanvas.setAttribute('style', `width:${this.model.get('width')}px; height:${this.model.get('height')}px`);
        }

        this._faerunHoverIndicator.setAttribute('id', 'hover-indicator');

        this._faerunContainer.appendChild(this._faerunHoverIndicator);
        this._faerunContainer.appendChild(this._faerunCanvas);

        this.el.appendChild(this._faerunContainer);

        var x = this.model.get('x');
        var y = this.model.get('y');
        var z = this.model.get('z');
        var c = this.model.get('c');

        if (z.length !== x.length) {
            z = [];
            for (var i = 0; i < x.length; i++) {
                z.push(0.0);
            }
        }

        var vertexCoordinates = { x: x, y: y, z: z }
        var edgeCoordinates = { x: [], y: [], z: [] }
        var colors = { r: [], g: [], b: [] }

        if (c.length === 0) {
            var rgb = TMAP.hexToRgb(this.model.get('color'));
            console.log("rgb", rgb);
            for (var i = 0; i < x.length; i++) {
                colors.r.push(rgb[0]);
                colors.g.push(rgb[1]);
                colors.b.push(rgb[2]);
            }
        } else {
            for (var i = 0; i < c.length; i++) {
                var rgb = c[i];
                colors.r.push(rgb[0]);
                colors.g.push(rgb[1]);
                colors.b.push(rgb[2]);
            }
        }

        var tmap = new TMAP(
            this._faerunCanvas,
            vertexCoordinates,
            edgeCoordinates,
            colors,
            null,
            this.model.get('background_color'),
            this.model.get('view')
        );

        tmap.faerun.el['hoverIndicator'] = this._faerunHoverIndicator;

        tmap.onVertexOver(e => {
            this.model.set('hovered_index', e.index);
            this.model.save_changes();
        });

        tmap.onVertexOut(() => {
            this.model.set('hovered_index', -1);
            this.model.save_changes();
        });

        tmap.onVertexClick(e => {
            this.model.set('selected_index', e.index);
            this.model.save_changes();
        });

        this.value_changed();

        // Observe changes in the value traitlet in Python, and define
        // a custom callback.
        this.model.on('change:value', this.value_changed, this);
    },

    value_changed: function () {
        // this.el.textContent = this.model.get('value');
    }
});


module.exports = {
    FaerunModel: FaerunModel,
    FaerunView: FaerunView
};
