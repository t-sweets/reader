import unicodedata
import zenhan


class ReceiptManager:
    def __init__(self, device, width=32, tab=25):
        device.jp_init()
        self.device = device
        self._set_tab(width, tab)

    def header(self, icon=None, date=None):
        self.device.jp_init()
        if icon is not None:
            self.device.image(icon, impl="bitImageColumn")
            self.device.text('\n')

        self.device.set(align='center')
        self.device.text_jp("ご利用ありがとうございます。\n\n")

        if date is not None:
            self.device.set(align='center')
            self.device.text_jp(date)

        self.device.text('\n\n')
        self.device.set(align='center')
        self.device.text_jp("領 収 証\n\n", dw=True)

    def item(self, name, price, pcs, unit):
        self.device.text_jp(name + '\n')
        self.device.set(align='right')
        self._set_tab(self.width, int(self.width / 2))
        self.device.text_jp("x{0}(@{1})\t￥{2}\n".format(str(pcs), str(unit), str(price)))

    def footer(self, total_price, payment_method='cash', cash=None, change=None, customer_id=None, balance=None):
        self._set_tab(self.width, int(self.width / 2))
        self.device.text_jp("\n合計", dw=True)
        self.device.set(bold=True)
        self.device.text_jp("\t" + self._set_price(total_price, zen=True) + "\n")
        self.device.set(bold=False)

        if payment_method is 'cash':
            self.device.text_jp("お預り\t" + self._set_price(cash, zen=True) + "\n")
            self.device.text_jp("お釣り\t" + self._set_price(change, zen=True) + "\n\n\n\n\n\n")
        else:
            self.device.text(payment_method)
            self.device.text_jp("支払\t" + self._set_price(total_price, zen=True) + '\n\n')
            self.device.text_jp(payment_method + "番号     " + customer_id + '\n')
            self.device.text_jp(payment_method + "残高\t" + self._set_price(balance) + '\n\n\n\n\n\n')

    def _set_tab(self, width, tab):
        self.area = tab
        self.width = width
        self.device.set_tab(tab)

    def _set_price(self, val, zen=False):
        prefix = '-' if val < 0 else '￥'
        string = prefix + "{:,d}".format(val)
        if zen:
            string = zenhan.h2z(string)
        space = (self.width - self.area) - (self.str_width(string))
        return (" " * space) + string

    @classmethod
    def str_width(cls, ustr):
        width = 0
        for c in ustr:
            cw = unicodedata.east_asian_width(c)
            if cw in u"WFA":
                width += 2
            else:
                width += 1
        return width

