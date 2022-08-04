$('#toogleIcon1').click(function () {
    $('#icon1').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
});

$('#toogleIcon2').click(function () {
    $('#icon2').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
});

$('#toogleIcon3').click(function () {
    $('#icon3').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
});

$('#toggleSummary').click(function () {
    $('#summary-icon').toggleClass('fa-chevron-up').toggleClass('fa-chevron-down');
      $("#toggleSummary #summary-btn-text").text($("#toggleSummary #summary-btn-text").text() == 'Show order summary' ? 'Hide order summary' : 'Show order summary');
});

$('.card-selector').click(function(event) {
  $('.card-selector').not(this).removeClass('card-clicked');
  $(this).toggleClass('card-clicked');
});


(function () {
    "use strict";
    var jQueryPlugin = (window.jQueryPlugin = function (ident, func) {
        return function (arg) {
            if (this.length > 1) {
                this.each(function () {
                    var $this = $(this);

                    if (!$this.data(ident)) {
                        $this.data(ident, func($this, arg));
                    }
                });

                return this;
            } else if (this.length === 1) {
                if (!this.data(ident)) {
                    this.data(ident, func(this, arg));
                }

                return this.data(ident);
            }
        };
    });
})();

(function () {
    "use strict";
    function Quantity($root) {
        const element = $root;
        const quantity = $root.first("data-quantity");
        const quantity_target = $root.find("[data-quantity-target]");
        const quantity_minus = $root.find("[data-quantity-minus]");
        const quantity_plus = $root.find("[data-quantity-plus]");
        var quantity_ = quantity_target.val();
        $(quantity_minus).click(function () {
            quantity_target.val(--quantity_);
        });
        $(quantity_plus).click(function () {
            quantity_target.val(++quantity_);
        });
    }
    $.fn.Quantity = jQueryPlugin("Quantity", Quantity);
    $("[data-quantity]").Quantity();
})();

