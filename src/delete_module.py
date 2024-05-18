def delete(button, sub_total, principal_result_label, total_result_label):

    sub_total.delete(0,'end')
    # total_result_label.config(text='', borderwidth=0, bg='#f1f1f0')
    principal_result_label.grid_forget()
    total_result_label.grid_forget()
    
    button.config(text='Bs', state='disabled')

    converted = False

    return converted