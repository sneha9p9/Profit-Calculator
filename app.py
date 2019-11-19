from flask import Flask

from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':

        #Request for input fields
        s_comm = float(request.form['s_comm'])
        i_s_price = float(request.form['i_s_price'])
        b_comm = float(request.form['b_comm'])
        c_ga_tax = float(request.form['c_ga_tax'])        
        company_symbol = request.form['company_symbol']
        allotment_number = float(request.form['allotment_number'])
        f_s_price = float(request.form['f_s_price'])


        #Applying all the formulas to calculate the price

        pro = int(allotment_number) * float(f_s_price)
        t_tax = (((float(f_s_price) - float(i_s_price)) * int(allotment_number) - float(b_comm) - float(s_comm)))
        tax = t_tax * float(c_ga_tax) / 100
        i_total = int(allotment_number) * float(i_s_price)
        cost = i_total + float(b_comm) + float(s_comm) + tax
        n_profit = pro - cost
        r_o_inv = n_profit / cost * 100
        b_reakeven = (i_total + float(b_comm) + float(s_comm)) / int(allotment_number)


        print_ret_on_inv = "%.2f" % r_o_inv + "%"
        print_pro = "$%.2f" % pro
        print_cost_1 = "$%.2f" % cost
        print_total_1 = str(allotment_number) + " x $" + str(i_s_price) + " = %.2f" % i_total
        print_gain_1 = str(c_ga_tax) + "% of $" + "%.2f" % t_tax + " = %.2f" % tax
        print_n_profit = "$" + "%.2f" % n_profit
        print_b_reakeven = "$" + "%.2f" % b_reakeven


        tempData = {'tickerSybol': company_symbol,
                   'finalShare_1': f_s_price, 'b_reakeven_1':print_b_reakeven, 'sellComm_1':s_comm,
                   'initShare_1':i_s_price, 'i_total_1': print_total_1, 'buyComm_1':b_comm,
                   'taxRate_1':c_ga_tax, 'pro_1':print_pro, 'allot_1': allotment_number, 'gain_1':print_gain_1,
                   'cost_1':print_cost_1, 'n_profit_1':print_n_profit,
                   'ret_on_inv_1':print_ret_on_inv}
        return render_template('index.html', **tempData)

if __name__ == '__main__':
    app.run(debug=True)
