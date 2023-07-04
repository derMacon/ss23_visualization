import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def getLines(rng, nLines, nPtsPerLine):
    x = np.linspace(*rng, num=nLines)
    y = np.linspace(*rng, num=nPtsPerLine)
    X, Y = np.meshgrid(x, y)
    X = X.transpose()
    Y = Y.transpose()
    return np.concatenate((X, Y)), np.concatenate((Y, X))


def getLines_new(uv_data, transformation_idx):
    x = uv_data[transformation_idx][0]
    y = uv_data[transformation_idx][1]

    X = x.transpose()
    Y = y.transpose()

    return np.concatenate((X, x)), np.concatenate((Y, y))


rng = [-1, 1]
nLines = 15
nPtsPerLine = 20

uv_data = np.load('../material/UVData.npz')['UVData']

fig = plt.figure(figsize=(8, 4))
fig.add_subplot(1, 2, 1, aspect=1.)
plt.title("identity")

X_0, Y_0 = getLines(rng, 15, 15)
# print('X: ', X.shape)
# print('X: ', X)


for i in range(5):
    X, Y = getLines_new(uv_data, i)
    # print('X: ', X)
    # print('X_0: ', X_0)

    for x, y in zip(X, Y):
        plt.plot(x, y, c="k")

plt.show()


# -------------- task 2 --------------


def PCA(dataMat, keep=None):
    nSamples, dim = dataMat.shape
    if dim < nSamples:
        if keep is None:
            keep = dim
        A = dataMat.transpose().dot(dataMat) / nSamples
        eigData = np.linalg.eigh(A)
        eigval = (eigData[0][-keep::])[::-1]
        eigvec = ((eigData[1][:, -keep::]).transpose())[::-1]
    else:
        if keep is None:
            keep = nSamples
        A = dataMat.dot(dataMat.transpose()) / nSamples
        eigData = np.linalg.eigh(A)
        eigval = (eigData[0][-keep::])[::-1]
        eigvec = ((eigData[1][:, -keep::]).transpose())[::-1]
        eigvec = np.einsum(eigvec, [0, 1], dataMat, [1, 2], [0, 2])
        normList = np.linalg.norm(eigvec, axis=1)
        eigvec = np.einsum(eigvec, [0, 1], 1 / normList, [0], [0, 1])
    return eigval, eigvec


uv_data_flat = []
for curr_uv_data in uv_data:
    tmp = np.array(curr_uv_data).flatten()
    uv_data_flat.append(tmp)

uv_data_flat = np.array(uv_data_flat)

# print('uv flat shape: ', uv_data_flat.shape)
# print('uv flat: ', uv_data_flat)

uv_mean = np.mean(uv_data_flat, axis=0)
uv_data_flat -= uv_mean

eigval, eigvec = PCA(uv_data_flat)
print('eigval.shape: ', eigval.shape)
print('eigval: ', eigval)

plt.scatter(np.arange(0, 100), eigval)
plt.show()

sum = np.sum(eigval)
print('sum: ', sum)

target = sum * 0.99
i = 0
while target >= 0 and i < eigval.shape[0]:
    target -= eigval[i]
    i += 1

print('99 percent: i == ', i)




# fig=plt.figure(figsize=(2*4,3))
# for i in range(5):
#     fig.add_subplot(1,2,i+1)
#     plt.title("mode {:d}".format(i+1))
#     scale=eigval[i]**0.5
#     vList=np.linspace(-1,1,num=7)
#     dataRe=np.einsum(eigvec[i],[0],vList*scale,[1],[1,0])
#     for v,y in zip(vList,dataRe):
#         plt.plot(x,y+mean,c=cm.coolwarm(0.5*v+0.5))
# plt.show()
