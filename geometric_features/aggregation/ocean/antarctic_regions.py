def antarctic(gf):
    """
    Aggregate Antarctic regions similar to Timmermann et al. (2013)

    Parameters
    ----------
    gf : geometric_features.GeometricFeatures
        An object that knows how to download and read geometric features

    Returns
    -------
    fc : geometric_features.FeatureCollection
        The new feature collection with antarctic regions
    """
    # Authors
    # -------
    # Xylar Asay-Davis

    regions = [
        'Southern Ocean',
        'Southern Ocean 60S',
        'Eastern Weddell Sea Shelf',
        'Eastern Weddell Sea Deep',
        'Western Weddell Sea Shelf',
        'Western Weddell Sea Deep',
        'Weddell Sea Shelf',
        'Weddell Sea Deep',
        'Bellingshausen Sea Shelf',
        'Bellingshausen Sea Deep',
        'Amundsen Sea Shelf',
        'Amundsen Sea Deep',
        'Eastern Ross Sea Shelf',
        'Eastern Ross Sea Deep',
        'Western Ross Sea Shelf',
        'Western Ross Sea Deep',
        'East Antarctic Seas Shelf',
        'East Antarctic Seas Deep',
        'A010',
        'A020',
        'A030',
        'A040',
        'A050',
        'A060',
        'A070',
        'A080',
        'A090',
        'A100',
        'A110',
        'A120',
        'A130',
        'A140',
        'A150',
        'A160',
        'A170',
        'A180',
        'A190',
        'A200',
        'A210',
        'A220',
        'A230',
        'A240',
        'A250',
        'A260',
        'A270',
        'A280',
        'A290',
        'A300',
        'A310',
        'A320'
    ]

    fc = gf.read(componentName='ocean', objectType='region',
                 featureNames=regions)

    return fc
