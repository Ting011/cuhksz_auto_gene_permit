from flask import Flask, render_template
import argparse
import time


app = Flask(__name__)

def get_args(): 
    t1 = time.strftime('%Y-%m-%d', time.localtime())
    t2 = time.strftime('%Y-%m-%d', time.localtime(time.time()+518400))
    parser = argparse.ArgumentParser(description='fake your passport')
    parser.add_argument('--name',required= True, help='fake name')
    parser.add_argument('--id', required= True,help='fake student id') 
    parser.add_argument('--start_date', help='your fake start date',
                        default=t1)
    parser.add_argument('--end_date', help='you fake end date',
                        default=t2)
    
    args = parser.parse_args()
    return args

@app.route('/', methods=['GET', 'POST'])
def main():
    arg = get_args()

    return render_template('view.html', student_id = str(arg.id),\
     student_name = str(arg.name),first_date = str(arg.start_date), last_date = str(arg.end_date))


if __name__ == '__main__':
    app.run()