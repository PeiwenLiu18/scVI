use_cuda = True

from scvi.dataset.BICCN import *
from scvi.dataset.dataset import GeneExpressionDataset
from scvi.harmonization.utils_chenling import run_model, eval_latent
import sys

model_type = str(sys.argv[1])
print(model_type)

plotname = 'Zeng'

dataset1 = Zeng10X()
# dataset1.subsample_cells(6274)
# dataset1.labels = dataset1.labels.reshape(len(dataset1.labels),1)
dataset2 = ZengSS2()
dataset1.subsample_genes(dataset1.nb_genes)
dataset2.subsample_genes(dataset2.nb_genes)
gene_dataset = GeneExpressionDataset.concat_datasets(dataset1, dataset2)
latent, batch_indices, labels, keys = run_model(model_type, gene_dataset, dataset1, dataset2, filename=plotname, ngenes=5000)
eval_latent(batch_indices, labels, latent, keys, plotname+'.'+model_type)


# Seurat
# asw 0.2694100999249462
# nmi 0.8200514733671972
# ari 0.7142208811694015
# uca 0.6899037196822223
# Entropy batch mixing : 0.6419939508089696

