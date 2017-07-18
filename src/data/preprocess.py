import click
import pandas as pd


def one_hot_encoder_values():
    global mssubclass
    mssubclass = 16
    global mszoning
    mszoning = 8
    global street
    street = 2
    global alley
    alley = 3
    global lotshape
    lotshape = 4
    global landcountour
    landcountour = 4
    global utilities
    utilities = 4
    global lotconfig
    lotconfig = 5
    global landslope
    landslope = 3
    global neighborhood
    neighborhood = 25
    global condition1
    condition1 = 10
    global condition2
    condition2 = 9
    global bldgtype
    bldgtype = 5
    global housestyle
    housetype = 8
    global roofstyle
    roofstyle = 6
    global roofmat1
    roofmat1 = 8
    global exterior1st
    exterior1st = 17
    global exterior2nd
    exterior2nd = 17
    global masvnrtype
    masvnrtype = 5
    global exterqual
    exterqual = 5
    global extercond
    extercond = 5
    global foundation
    foundation = 6
    global bsmtqual
    bsmtqual = 6
    global bsmtcond
    bsmtcond = 6
    global bsmtexposure
    bsmtexposure = 5
    global bsmtfintype1
    bsmtfintype1 = 7
    global bsmtfintype2
    bsmtfintype2 = 7
    global heating
    heating = 6
    global heatingqc
    heatingqc = 5
    global centralair
    centralair = 2
    global electrical
    electrical = 5
    global kitchen_quality
    kitchen_quality = 5
    global functional
    functional = 8
    global fireplace_qu
    fireplace_qu = 6
    global garage_type
    garage_type = 7
    global garage_finish
    garage_finish = 4
    global garage_qual
    garage_qual = 6
    global garage_condition
    garage_condition = 6
    global paved_drive
    paved_drive = 3
    global pool_qc
    pool_qc = 5
    global fence
    fence = 5
    global misc_feature
    misc_feature = 6
    global sale_type
    sale_type = 10
    global sale_condition
    sale_condition = 6


def get_featues(dframe):
    return dframe[['x0', 'x1', 'x2', 'x3']]


def get_label(dframe):
    return dframe['y']


def read_raw_data(fname='data/raw/train.csv'):
    dframe = pd.read_csv(fname, header=None)
    return dframe


# def preprocess_data(dframe):
#    dframe = dframe.copy()  # I want to avoid inplace modifications
#    dframe.columns = ['x0', 'x1', 'x2', 'x3', 'y']
#    return dframe


def read_processed_data(fname='data/processed/processed.pickle'):
    dframe = pd.read_pickle(fname)
    return dframe


@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True, dir_okay=False))
# @click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
# @click.option('--excel', type=click.Path(writable=True, dir_okay=False))
# def main(input_file, output_file, excel):

def main(input_file):
    print('Preprocessing data')

    dframe = read_raw_data(input_file)
    get_null_count(dframe)


#    dframe = preprocess_data(dframe)

#    dframe.to_pickle(output_file)
#    if excel is not None:
#        dframe.to_excel(excel)

def get_null_count(dframe):
    null_counts = dframe.isnull().sum()
    print(null_counts[null_counts > 0])
    return null_counts[null_counts > 0].count()

if __name__ == '__main__':
    main()
