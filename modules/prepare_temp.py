from torchvision import transforms as transforms


class Preparation:
    def __init__(self):
        self.TRANS_CROP = {
            "CenterCrop": "CenterCrop",
            "FiveCrop": "FiveCrop",
            "TenCrop": "TenCrop",
            "Resize": "Resize",
        }

        self.TRANS_FILTER = {
            "Grayscale": "Grayscale",
            "GaussianBlur": "GaussianBlur",
        }

        self.TRANS_CROPS = self.TRANS_CROP.values()
        self.TRANS_FILTERS = self.TRANS_FILTER.values()

    def setting_crop_prepare(self, prepare, scope):
        """
        Cropの前処理を設定します。
        """
        if prepare == self.TRANS_CROP["CenterCrop"]:
            transform = transforms.CenterCrop(scope)
        elif prepare == self.TRANS_CROP["FiveCrop"]:
            transform = transforms.FiveCrop(scope)
        elif prepare == self.TRANS_CROP["TenCrop"]:
            transform = transforms.TenCrop(scope)
        elif prepare == self.TRANS_CROP["Resize"]:
            transform = transforms.Resize(scope)
        return transform

    def setting_filter_prepare(self, prepare, kernel_size, sigma_min, sigma_max):
        """
        Filterの前処理を設定します。
        """
        if prepare == self.TRANS_FILTER["Grayscale"]:
            transform = transforms.Grayscale()
        elif prepare == self.TRANS_FILTER["GaussianBlur"]:
            transform = transforms.GaussianBlur(
                kernel_size=kernel_size, sigma=(sigma_min, sigma_max)
            )
        return transform
