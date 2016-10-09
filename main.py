import stft
import scipy.io.wavfile
import scipy.misc
import pylab
import numpy as np
from utility import pcm2float, float2pcm
import cv2
import libtiff


def save_image(data, file_name):
    print(data.dtype, data.shape)
    cv2.imwrite(file_name, data)
    pass

def read_image(file_name):
    return cv2.imread(file_name)

sample_file = 'Duke Ellington - Rext.wav'
rate, data =  scipy.io.wavfile.read(sample_file)

data = data[:,0]
assert isinstance(data, np.ndarray)
data = pcm2float(data)
print(data.dtype)

x = data
fs = rate # sampled at 8 kHz

samples = len(x)
T = 60
frame_length = 0.1
hop_length = frame_length
t = scipy.linspace(0, T, samples, endpoint=False)
x = x[:T*rate]

X = stft.stft(x, fs, frame_length, hop_length)
print(X.dtype)
print(np.max(X.real),np.min(X.real))
print(np.max(X.imag),np.min(X.imag))

normal = lambda x:(x+300)/600
inv_normal = lambda x:x*600 - 300

X_image = cv2.merge([normal(X.real) * 65535, normal(X.imag) * 65535, np.zeros(X.shape[:2])])
print(np.max(X_image[:,:,0]),np.min(X_image[:,:,0]))
print(np.max(X_image[:,:,1]),np.min(X_image[:,:,1]))
X_image = X_image.astype('uint16')
print("finished stft.")
test_image = scipy.misc.imread("test.png")
print(test_image.dtype, test_image.shape)
print(X_image.dtype, X_image.shape)
# Plot the magnitude spectrogram.
pylab.figure()
pylab.imshow(X_image)
save_image(X_image, 'test1.tiff')
X_image = read_image('test1.tiff')
pylab.show()
print("show result of stft.")

print(X_image.dtype, X_image.shape)
new_X = np.zeros(X_image.shape[:2], 'complex128')
new_X.real = inv_normal(X_image[:,:,0].astype('float64') / 65535)
new_X.imag = inv_normal(X_image[:,:,1].astype('float64') / 65535)
print(np.max(new_X.real),np.min(new_X.real))
print(np.max(new_X.imag),np.min(new_X.imag))
# Compute the ISTFT.
xhat = stft.istft(new_X, fs, T, hop_length)
print("finished istft.")

# Plot the input and output signals over 0.1 seconds.
T1 = int(0.1 * fs)

pylab.figure()
pylab.plot(t[:T1], x[:T1], t[:T1], xhat[:T1])
pylab.xlabel('Time (seconds)')

pylab.figure()
pylab.plot(t[-T1:], x[-T1:], t[-T1:], xhat[-T1:])
pylab.xlabel('Time (seconds)')
pylab.show()
print("show result of istft.")
xhat = float2pcm(xhat)
print(xhat.dtype)
scipy.io.wavfile.write("after-" + sample_file, rate, xhat)
print("saved result istft.")
