from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
# print modules
__all__ = [basename(f)[:-3] for f in modules if isfile(f)]

# print(f'all={__all__}')
