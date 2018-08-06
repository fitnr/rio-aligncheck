import logging

import rasterio
from affine import UndefinedRotationError

__author__ = "Neil Freeman"
__version__ = '1.0.0'

HEADER = "path", "epsg", "origin-x", "origin-y", "pixelsize-x", "pixelsize-y"
ROWFORMAT = "{path}\t{0[epsg]}\t{0[origin][0]}\t{0[origin][1]}\t{0[pixel size][0]}\t{0[pixel size][1]}"


def get_meta(raster):
    with rasterio.open(raster) as src:
        return {
            'epsg': src.profile['crs'].to_epsg(),
            'origin': (
                src.transform.xoff / src.transform[0],
                src.transform.yoff / -src.transform[4]
            ),
            'pixel size': (src.transform[0], -src.transform[4]),
        }


def check_alignment(rasters, **kwargs):
    metas = {raster: get_meta(raster) for raster in rasters}
    result = []

    keys = 'epsg', 'origin', 'pixel size'

    if kwargs.get('full_report'):
        if kwargs.get('header'):
            result.append("\t".join(HEADER))

        for path, m in metas.items():
            result.append(ROWFORMAT.format(m, path=path))

    elif kwargs.get('report'):
        distinct = [
            dict(d) for d in
            list(set([tuple((k, m[k]) for k in keys) for m in metas.values()]))
        ]
        for path, m in metas.items():
            for d in distinct:
                if all(d[k] == m[k] for k in keys):
                    result.append('{}\t{}'.format(1 + distinct.index(d), path))
                    break

    else:
        for k in keys:
            attrs = set([m[k] for m in metas.values()])
            if len(attrs) > 1:
                result.append('{} count: {}'.format(k, len(attrs)))

    return result
