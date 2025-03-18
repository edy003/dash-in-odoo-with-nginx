odoo.define('my_dash_module.dashboard', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    
    publicWidget.registry.DashboardWidget = publicWidget.Widget.extend({
        selector: '.container',
        start: function () {
            var self = this;
            this.$el.find('#dash_iframe').on('load', function () {
                self._resizeIframe();
            });
            return this._super.apply(this, arguments);
        },
        _resizeIframe: function () {
            // Ajustez la hauteur si nécessaire
            var iframe = this.$el.find('#dash_iframe');
            iframe.css('height', $(window).height() - 200 + 'px');
        },
    });
});