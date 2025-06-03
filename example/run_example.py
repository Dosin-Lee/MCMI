import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import numpy as np
from mcmi import mcmi


def load_vcf(path):
    samples = []
    genos = []
    with open(path) as f:
        for line in f:
            if line.startswith('##'):
                continue
            if line.startswith('#CHROM'):
                parts = line.strip().split('\t')
                samples = parts[9:]
            else:
                parts = line.strip().split('\t')
                row = []
                for val in parts[9:]:
                    ds = val.split(':')[1]
                    row.append(float(ds))
                genos.append(row)
    X = np.array(genos).T
    return samples, X


def load_pheno(path):
    names = []
    values = []
    with open(path) as f:
        next(f)
        for line in f:
            name, val = line.strip().split('\t')
            names.append(name)
            values.append(float(val))
    return names, np.array(values)


if __name__ == '__main__':
    sample_names, X = load_vcf(os.path.join('input', 'test.vcf'))
    pheno_names, y = load_pheno(os.path.join('input', 'phenotype.tsv'))
    order = [sample_names.index(n) for n in pheno_names]
    X = X[order]
    selected = mcmi(X, y, max_features=2)
    os.makedirs('output', exist_ok=True)
    with open(os.path.join('output', 'results.txt'), 'w') as f:
        f.write('Selected feature indices: ' + ','.join(map(str, selected)) + '\n')
    print('Selected features:', selected)
    print('Results written to results.txt')
