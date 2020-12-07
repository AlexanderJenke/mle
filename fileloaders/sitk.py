import SimpleITK as sitk
from numpy import ndarray, transpose
from torch import Tensor


class SITKFile:
    def __init__(self, path: str, file: sitk.Image):
        self.path = path
        self.file = file
        self.volume = sitk.GetArrayFromImage(self.file).transpose((1, 2, 0))
        self.spacing = self.file.GetSpacing()

    def write_data(self, volume: ndarray or Tensor, file_name: str):
        """
        Creates a file containing the given volume while copying the meta data from the called object
        :param volume: image data to be writen to the file
        :param output_file: path to the file to be written

        """
        if isinstance(volume, Tensor):
            volume = volume.detach().cpu().numpy()
        image = sitk.GetImageFromArray(transpose(volume, (2, 0, 1)))
        image.CopyInformation(self.file)
        sitk.WriteImage(image, file_name)

class NIFTI(SITKFile):
    """
    SimpleITK Image from a file
    """
    def __init__(self, path):
        """
        Reads an image from a file
        :param path: file to be read
        """
        super().__init__(path=path, file=sitk.ReadImage(path))



class TempNIFTI(SITKFile):
    """
    SimpleITK Image from a file
    """
    def __init__(self, path):
        """
        Reads an image from a file
        :param path: file to be read
        """
        super().__init__(path=path, file=sitk.GetImageFromArray([[[0]]]))
        del self.volume


    def __getattr__(self, item):
        if item == "volume":
            return sitk.GetArrayFromImage(sitk.ReadImage(self.path)).transpose((1, 2, 0))
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")



class DICOM(SITKFile):
    """
    SimpleITK Image from a Series
    """
    def __init__(self, directory):
        """
        Reads an image from an image series
        :param directory: directory containing the image series
        """
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(directory)
        reader.SetFileNames(dicom_names)
        reader.MetaDataDictionaryArrayUpdateOn()
        super().__init__(path=directory, file=reader.Execute())