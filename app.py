from flask import Flask,render_template,request
import pandas as pd 
import csv

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/data',methods=['GET','POST'])
def data():
	#POsT request to display the csv file
	if request.method == 'POST':
		f = request.form['csvfile']
		data = []
		with open(f) as file:
			csvfile = csv.reader(file)
			for row in csvfile:
				data.append(row)
	    #Pandas dataframe to seperate different column in well manner			
		data = pd.DataFrame(data)			
		return render_template('data.html',data=data.to_html(header=False, index=False))																							

if __name__ == '__main__':
	app.run(debug=True)    
