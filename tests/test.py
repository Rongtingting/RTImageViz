# %%
import tifffile
segmentation_mask = tifffile.imread("/mnt/nfs/home/rongtinghuang/Results/EC_MIBI_Data/Pembro/Segmentation_learn/01_image_ometiff/251110_test2/segmentation_mask.tiff")

# %%
from rtimageviz.utils.pyqupath.geojson import mask_to_geojson_joblib
# %%
mask_to_geojson_joblib(segmentation_mask, "/mnt/nfs/home/rongtinghuang/TMP_VIEW/segmentation_mask.geojson", n_jobs=8)
# %%
