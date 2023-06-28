import numpy as np
import matplotlib.pyplot as plt


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

rng=[-1,1]
nLines=15
nPtsPerLine=20


uv_data = np.load('../material/UVData.npz')['UVData']
print('shape: ', uv_data.shape)

fig=plt.figure(figsize=(8,4))
fig.add_subplot(1,2,1,aspect=1.)
plt.title("identity")


X_0, Y_0 = getLines(rng, 15, 15)
# print('X: ', X.shape)
# print('X: ', X)


for i in range(5):
    X, Y = getLines_new(uv_data, i)
    print('X: ', X)
    print('X_0: ', X_0)

    for x,y in zip(X,Y):
        plt.plot(x,y,c="k")

plt.show()
