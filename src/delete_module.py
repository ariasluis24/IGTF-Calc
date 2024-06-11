def delete(button, sub_total, principal_result_label, total_result_label, agent_of_retention, IGTF_label):

    sub_total.delete(0,'end')
    # total_result_label.config(text='', borderwidth=0, bg='#f1f1f0')
    principal_result_label.grid_forget()
    total_result_label.grid_forget()
    agent_of_retention.config(text='', bg='#f1f1f0')
    IGTF_label.config(text='', bg='#f1f1f0')
    button.config(text='Bs', state='disabled')

    converted = False

    return converted

def delete_second_UI(sub_total, result):
    sub_total.delete(0, 'end')
    result.grid_forget()