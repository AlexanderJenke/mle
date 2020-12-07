from os import listdir
from os.path import join, isfile

from torch.utils.data import Dataset

from mle.fileloaders import NIFTI


class Patients(Dataset):
    def __init__(self, directory: str, file_name: str, fileloader=NIFTI):
        self.data = {}

        for pat_id in listdir(directory):
            file_path = join(directory, pat_id, file_name)
            if isfile(file_path):
                self.data[pat_id] = fileloader(path=file_path)
            else:
                print(f"{join(directory, pat_id, file_name)} does not exist!")

        self.keys = sorted(self.data.keys())

    def __getitem__(self, index):
        return self.data[self.keys[index]].volume

    def getVolumeByKey(self, key):
        return self.data[key].volume

    def __len__(self):
        return len(self.keys)


if __name__ == '__main__':
    d = Patients("/home/jenkealex/workspace/g27dl02/dual_energy/Patients/valid/", "D34/140kVp_16x12/low_img.nii.gz")
    for _ in d:
        pass
    print(d)
