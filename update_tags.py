import os
from geometric_features import GeometricFeatures
from geometric_features.utils import write_feature_names_and_tags


# Write a file features_and_tags.json with features and tags from the cache.
# This updates the file names, feature names and tags that geometric_features
# knows about.
write_feature_names_and_tags('./geometric_data')

# move features_and_tags.json into geometric_features to replace the old
# manifest
os.rename('features_and_tags.json',
          'geometric_features/features_and_tags.json')
