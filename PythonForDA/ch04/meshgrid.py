points = np.arange(-5, 5, 0.01)
points.shape
points.ndim
points
xs, ys = np.meshgrid(points, points)
xs.shape
ys.shape
xs
ys.shape
ys
z = np.sqrt(x**2 + y**2)
import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
z.shape
z = np.sqrt(xs**2 + ys**2)
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
