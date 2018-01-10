import ui
import os
import sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import *

from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
from PyQt4 import QtGui, QtCore

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
from PyQt4 import QtGui,QtCore
from IPython.display import Audio
import wave
import os
import struct
import numpy as np
from scipy.io.wavfile import read,write
from scipy.fftpack import fft
import pylab as plt
from scipy.fftpack import rfft, irfft, fftfreq , fftshift , ifft,fft
import scipy.io.wavfile
import wave
import os
from scipy.io import wavfile as wav #libraries to upload .wav sound file
from IPython.display import Audio
import sounddevice as sd


NewArray=np.array
FourierArray=np.array
fig1=Figure()

class hello(QtGui.QMainWindow, ui.Ui_Form):
	def __init__(self):

		super(hello, self).__init__()
		self.setupUi(self)
       # self.widget.setStyleSheet(_fromUtf8("border-image: url(:/image/47383964-dj-image.jpg) 0 0 0 0 stretch stretch;"))
		self.Import.clicked.connect(self.btn_browse_fn)#Button Import is clicked
		self.ShowFrequencies.clicked.connect(self.FrequenciesFunction)#Button ShowFrequencies is clicked
		self.Save.clicked.connect(self.SaveFunction)#Button ShowFrequencies is clicked

		self.two.valueChanged.connect(self.valuechange)#any slider is changed
		self.four.valueChanged.connect(self.valuechange)
		self.six.valueChanged.connect(self.valuechange)
		self.eight.valueChanged.connect(self.valuechange)
		self.ten.valueChanged.connect(self.valuechange)
		self.twelve.valueChanged.connect(self.valuechange)
		self.fourteen.valueChanged.connect(self.valuechange)
		self.sixteen.valueChanged.connect(self.valuechange)
		self.eighteen.valueChanged.connect(self.valuechange)
		self.twenty.valueChanged.connect(self.valuechange)
	

	def btn_browse_fn(self):
		filePath = QtGui.QFileDialog.getOpenFileNames(self, 'Choose a file', "/home/hossam/QT/Equilizer", '*.WAV') #get file path
        
		fileName = ''.join(map(str, filePath)) #get file name

		self.ImportFunction(filePath,fileName) #Call function To import the selected file

	def ImportFunction(self,filePath,fileName):
		#global values decleration to be used in all functions
		global samples	#data array
		global time 	#file lenght in seconds
		global length 	#file number of samples
		global FSample 	#sampling frequency

		sys.path.append(str(filePath)) #add the chosen files path to system directory

		FSample, samples = read(str(fileName)) #read .wav sound file samples

		time = (len(samples))/float(FSample) #Calculate files duration

		length = len(samples) #calculating files lenght
		print("imported")	
		

		fig1 = Figure() #define a new figure
		fig1.patch.set_facecolor('white') #set backcolor to white
		ax1f1 = fig1.add_subplot(111)  #define a subplot 

		ax1f1.plot(samples)	#plot samples
		self.axis  =ax1f1	#define a self variable to hold the plot
		self.canvas = FigureCanvas(fig1) 
		self.mplvl.addWidget(self.canvas) #Pass the figure to the added widget (mplvl)
		self.canvas.draw() #show the drawing

		sd.play(samples,FSample) #play the imported file


		self.Import.setEnabled(False); 	#disable the import button



	def FrequenciesFunction(self):	#called when the show frequincies button is clicked

		global FourierArray 	#deal with the global fourierarray 
		FourierArray = fft(samples) #store the fourier transform of the wave file data into the array FourierArray
		print("Fourier transformed")
		self.valuechange() #call the valuechange function


		#Plot FourierArray

	def valuechange(self):  #called from the FrequenciesFunction or from any sliders movement
		
		global NewArray		#deal with the global NewArray
		global FourierArray #deal with the global fourierarray (where fourier transformed data is stored)
		
		NewArray = FourierArray[0:length].copy() #Save a copy from the fourierArray to avoid over writing on the original data

	



		NewArray[0:length/22] = (FourierArray[0*length/22:1*length/22].copy())*self.two.value()
		NewArray[1*length/22:2*length/22] = (FourierArray[1*length/22:2*length/22].copy())*self.four.value()
		NewArray[2*length/22:3*length/22] = (FourierArray[2*length/22:3*length/22].copy())*self.six.value()
		NewArray[3*length/22:4*length/22] = (FourierArray[3*length/22:4*length/22].copy())*self.eight.value()
		NewArray[4*length/22:5*length/22] = (FourierArray[4*length/22:5*length/22].copy())*self.ten.value()
		NewArray[5*length/22:6*length/22] = (FourierArray[5*length/22:6*length/22].copy())*self.twelve.value()
		NewArray[6*length/22:7*length/22] = (FourierArray[6*length/22:7*length/22].copy())*self.fourteen.value()
		NewArray[7*length/22:8*length/22] = (FourierArray[7*length/22:8*length/22].copy())*self.sixteen.value()
		NewArray[8*length/22:9*length/22] = (FourierArray[8*length/22:9*length/22].copy())*self.eighteen.value()
		NewArray[9*length/22:10*length/22] = (FourierArray[9*length/22:10*length/22].copy())*self.twenty.value()
		NewArray[10*length/22:11*length/22] = (FourierArray[10*length/22:11*length/22].copy())

		NewArray[11*length/22:12*length/22] = NewArray[10*length/22:11*length/22]
		NewArray[12*length/22:13*length/22] = NewArray[9*length/22:10*length/22]
		NewArray[13*length/22:14*length/22] = NewArray[8*length/22:9*length/22]
		NewArray[14*length/22:15*length/22] = NewArray[7*length/22:8*length/22]
		NewArray[15*length/22:16*length/22] = NewArray[6*length/22:7*length/22]
		NewArray[16*length/22:17*length/22] = NewArray[5*length/22:6*length/22]
		NewArray[17*length/22:18*length/22] = NewArray[4*length/22:5*length/22]
		NewArray[18*length/22:19*length/22] = NewArray[3*length/22:4*length/22]
		NewArray[19*length/22:20*length/22] = NewArray[2*length/22:3*length/22]
		NewArray[20*length/22:21*length/22] = NewArray[1*length/22:2*length/22]
		NewArray[21*length/22:22*length/22] = NewArray[0:(length/22)+1]





		self.axis.cla() #clear old drawings
		self.axis.plot(NewArray[0:11*length/22]) #draw half the fourier array after muliplying each band by its sliders value
		self.canvas.draw() #show the new drawing




	def SaveFunction(self): #called when the save button is clicked
		global NewArray #deal with the global NewArray (holds the fourier array after multiblying by the sliders values)
		OutArray = (ifft(NewArray.copy())).real #save the real values of the inverse fourier transfere of the array NewArray

		scaled = (OutArray / (0.85* np.max(np.abs(OutArray)))) #normalize data

		sd.play( scaled, FSample) #play the output data after normalization 
		

		scipy.io.wavfile.write('noise.wav', FSample, scaled) #save the file after modification into noise.wav
		print("saved")
		
		
		self.axis.cla()		#clear old figures
		self.axis.plot(scaled) #draw the new data
		self.canvas.draw()	#show the drawing

def main():
	App = QtGui.QApplication(sys.argv)
	form = hello()
	form.show()
	App.exec_()


if __name__ == '__main__':
	main()





