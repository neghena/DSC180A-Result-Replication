#!/usr/bin/env python

import sys
import json

#sys.path.insert(0, 'src/data')
#sys.path.insert(0, 'src/analysis')
#sys.path.insert(0, 'src/model')

from data/etl import get_data
from analysis/analysis import compute_aggregates
from model/model import train
from clean_gps import clean_gps


def main(targets):
    '''
    Runs project pipeline & depending on which targets
    it will run different sections of the project.

    `main` runs the targets in order of x=>y=>z.
    '''

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        data = get_data(**data_cfg)

    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)

        # make the data target
        compute_aggregates(data, **analysis_cfg)

    if 'model' in targets:
        with open('config/model-params.json') as fh:
            model_cfg = json.load(fh)

        # make the data target
        train(data, **model_cfg)

    if 'report' in targets:
        with open('notebooks/report.ipynb') as fh:
            report_cfg = json.load(fh) # how do you just open a jupyter notebook/turn it into a pdf?

    if 'clean_gps' in targets:
        with open('config/clean_gps_and_imu_data.json') as fh:
            clean_gps_cfg = json.load(fh)

        clean_gps(data, **clean_gps_cfg)

    return


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
