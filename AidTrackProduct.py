from tkinter import *
from AidTrackNetworkUtils import *

import AidTrackProductDetails

class ProductUi(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.geometry('750x550+200+300')
        self.parent.title('AidTrack')  # Title
        self.parent.iconbitmap('logo1icon.ico')
        self.parent.configure(background='white')
        self.pack(fill=BOTH, expand=True)

        Label(self, text="Item Id:").pack(side=TOP)
        self.productNumber = Entry(self)
        self.productNumber.pack(side=TOP)
        buttonTrack = Button(self, text='Track Product', command=self.track).pack(side=TOP)

    def track(self):
        item = self.productNumber.get()
        itemDetails = getItemJson(item)
        productDetails = getProductJson(itemDetails["product_id"])
        shipmentDetails = getShipmentJson(itemDetails["shipment_id"])
        campaignDetails = getCampaignJson(shipmentDetails["campaign_id"])
        AidTrackProductDetails.mainTk(Toplevel(), itemDetails, productDetails, shipmentDetails, campaignDetails)
        print("Track Product", productDetails)

def mainTk(root):
    app = ProductUi(root)
    root.mainloop()

def main():
    root = Tk()
    app = ProductUi(root)
    root.mainloop()

if __name__ == '__main__':
    main()
