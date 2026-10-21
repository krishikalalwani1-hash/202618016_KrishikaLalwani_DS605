# DS605 Lab 7: Image Representation, PCA, Eigenfaces and Face Recognition

**Dataset:** AT&T (ORL) Database of Faces: 40 subjects x 10 images, each 112 x 92 grayscale.

## Objective
Represent face images numerically, reduce their dimensionality with PCA/eigenfaces (implemented with NumPy), perform face matching in the reduced space, and compare it with traditional machine-learning classifiers.

## Approach

### Part A: Image representation
- Read every image as a grayscale pixel matrix (112 x 92, intensity 0 to 251).
- Flattened each image into a 10304-dimensional vector, giving a feature matrix `X` of shape (400, 10304) and a label vector `y` (subject IDs 1 to 40).
- Created a reproducible stratified per-subject split: 8 images per person for training and 2 for testing (320 train / 80 test), random seed 42. Every subject appears in both sets, and the code asserts that no image is in both.

### Part B: PCA, eigenfaces and compression
- Computed the mean face and centered the data using the training images only.
- Obtained the principal directions two ways, both with NumPy: (1) eigendecomposition of the covariance matrix, using the small 320 x 320 Gram-matrix trick because the full 10304 x 10304 covariance matrix is very large, and (2) SVD of the centered data matrix.
- Plotted cumulative explained variance and kept the minimum number of components preserving at least 90% variance: **k = 98** (90.03% variance retained).
- Reshaped principal components into images to visualize the eigenfaces.
- Projected train and test faces into PCA space (saved as `.npy` files), reconstructed sample faces, and compared reconstruction error and storage with the original pixel representation.

### Part C: Recognition in PCA space
- For each test image: subtract the training mean face, project onto the k eigenfaces, and find the closest stored training face by Euclidean distance. The label of that training face is the prediction.
- Repeated the same nearest-neighbor matching on raw pixels for comparison.

### Part D: Traditional machine learning
- Trained KNN, Logistic Regression and SVM on the PCA features (scikit-learn is used only for this comparison and for cross-validation).
- Chose the number of components and the model settings with stratified 4-fold cross-validation on the training set only.
- Evaluated the final models once on the test set.

## Results

| Method | Features per image | Test accuracy |
|---|---|---|
| NN on raw pixels (baseline) | 10304 | 100.00% |
| NN on PCA (baseline, k=98) | 98 | 98.75% |
| KNN (tuned, k=50) | 50 | 98.75% |
| Logistic Regression (tuned, k=50) | 50 | 97.50% |
| SVM (tuned, k=50) | 50 | 97.50% |

The full table is saved in `results_table.csv`.

Tuned settings (chosen by cross-validation, using k = 50 components):
- KNN: n_neighbors = 1, weights = uniform
- Logistic Regression: C = 10
- SVM: kernel = rbf, C = 10, gamma = 0.01

## Figures
| File | Description |
|---|---|
| `explained_variance.png` | Cumulative explained variance with the 90% threshold and chosen k |
| `eigenfaces.png` | Top 16 eigenfaces |
| `reconstructions.png` | Face reconstructions for different numbers of components |
| `matches_pca.png` | Examples of correct and incorrect matches |
| `accuracy_vs_components.png` | Cross-validated accuracy against number of components |

## Observations
- **Eigendecomposition vs SVD:** The eigenvalues from the two methods matched (`np.allclose` = True). The first five eigenvectors had an absolute cosine similarity of at least 1.0000, so the directions agree up to a sign flip. SVD is simpler and more numerically stable, while the covariance route needs the Gram-matrix trick to be practical.
- **Variance and compression:** 98 components preserve 90.03% of the variance. Each face shrinks from 10304 numbers to 98, about 105.1x smaller. Counting the stored eigenfaces and mean face, total storage is about 3.14x smaller than the raw training matrix.
- **Reconstruction:** At k = 98 the average reconstruction RMSE on the training faces is 12.44 gray levels (0 to 255 scale). Reconstruction error falls as more components are kept, and `reconstructions.png` shows faces becoming sharper as k grows.
- **Recognition:** Nearest neighbor on raw pixels reached 100.00% and on PCA features reached 98.75% (PCA features gave slightly lower accuracy than raw pixels), while using 98 instead of 10304 features per face. Matching time was 0.51934 s on raw pixels vs 0.00106 s in PCA space. In PCA space 1 of 80 test images were misidentified; examples are shown in `matches_pca.png`.
- **Classifiers:** The best classifier was KNN (tuned, k=50) with 98.75% test accuracy, which matched the nearest-neighbor baseline (98.75%).
- **Number of components:** Cross-validated accuracy on the training set reaches within one percentage point of its best value at about k = 30 components, so a compact representation retains most of the recognition accuracy (see `accuracy_vs_components.png`).


## Notes
- PCA, eigenfaces, projection and reconstruction are implemented with NumPy linear algebra only. Scikit-learn is used only for the final traditional-ML comparison and cross-validation.
- The mean face, PCA and all hyperparameter choices used the training data only. The test set was used once for the final evaluation.
- Random seed 42 is used for the train-test split and the cross-validation folds, so results are reproducible.
