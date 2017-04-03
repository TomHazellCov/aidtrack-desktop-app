from tkinter import *


class ProductDetailsUi(Frame):
    def __init__(self, parent, itemDetails, productDetails, shipmentDetails, campaignDetails):
        Frame.__init__(self, parent)
        self.parent = parent
        self.itemDetails = itemDetails
        self.productDetails = productDetails
        self.shipmentDetails = shipmentDetails
        self.campaignDetails = campaignDetails
        self.initUI()

    def initUI(self):
        self.parent.geometry('750x550+200+300')
        self.parent.title('AidTrack')  # Title
        self.parent.iconbitmap('logo1icon.ico')
        self.parent.configure(background='white')
        self.pack(fill=BOTH, expand=True)

        # tempFrame = Frame(self)
        # tempFrame.pack(fill=X)
        # Label(tempFrame, text="Item Id: " + self.itemDetails["id"]).pack(side=LEFT, padx=5, pady=5)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Product", font=("Helvetica", 20)).pack(side=LEFT, padx=5, pady=10)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Name: " + self.productDetails["product_name"]).pack(side=LEFT, padx=5, pady=5)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Description: " + self.productDetails["product_description"]).pack(side=LEFT, padx=5, pady=5)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Made By: " + self.productDetails["manufacturer"]["manufacturer_name"]).pack(side=LEFT, padx=5, pady=5)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Shipment", font=("Helvetica", 20)).pack(side=LEFT, padx=5, pady=10)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Name: " + self.shipmentDetails["shipment_title"]).pack(side=LEFT, padx=5, pady=5)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Part Of Campaign: " + self.campaignDetails["campaign_name"]).pack(side=LEFT, padx=5, pady=5)

        tempFrame = Frame(self)
        tempFrame.pack(fill=X)
        Label(tempFrame, text="Campaign created by: User" + self.campaignDetails["created_by"]).pack(side=LEFT, padx=5, pady=5)




        # Label(self, text="Item Id:").pack(side=TOP)
        # self.productNumber = Entry(self)
        # self.productNumber.pack(side=TOP)
        # buttonTrack = Button(self, text='Track Product', command=self.track).pack(side=TOP)

    # def track(self):
    #     item = self.productNumber.get()
    #     print("Track Product", item)

def mainTk(root, details, productDetails, shipmentDetails, campaignDetails):
    app = ProductDetailsUi(root, details, productDetails, shipmentDetails, campaignDetails)
    root.mainloop()

def main():
    root = Tk()
    # app = ProductDetailsUi(root, "")TODO mock it out
    root.mainloop()

if __name__ == '__main__':
    main()
