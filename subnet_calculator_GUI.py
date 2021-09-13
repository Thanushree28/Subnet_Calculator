import tkinter as tk

win = tk.Tk()
win.title("Subnet Calculator")
win.geometry("600x400")
win.configure(bg="grey")

ip = tk.StringVar(win)
subnet = tk.IntVar(win)
netw =tk.StringVar(win)
broad= tk.StringVar(win)
avail_host = tk.StringVar(win)
rang = tk.StringVar(win)



def net_addr(ip,sub):
	subnet = 32
	mask = sub
	lst = []
	netd = []
	network = []
	for i in range(0,mask): # appending mask value 1
		lst.append("1")
	sp = "".join(lst)
	for  i in range(0,subnet): # appending value 0
		if len(lst) < subnet:
			lst.append("0")
	sp1 ="".join(lst)
	print(ip,"ip")
	for i in range(0,len(sp1),8):
		netd.append(int(sp1[i:i+8],2))
	print(netd,"subnet")
	for j in range(4):
		network.append(ip[j] & netd[j])
	return network

def broad_addr(ip,sub):
	subnet = 32
	mask = sub
	lst = []
	bro = []
	broad = []
	for i in range(0,mask): # appending mask value 0
		lst.append("0")
	sp = "".join(lst)
	for  i in range(0,subnet): # appending value 1
		if len(lst) < subnet:
			lst.append("1")
	sp1 ="".join(lst)
#	print(ip,"ip")
	for i in range(0,len(sp1),8):
                bro.append(int(sp1[i:i+8],2))
#	print(bro,"subnet")
	for j in range(4):
		broad.append(ip[j] | bro[j])
	return broad

def available_host(ip,sub):
	subnet = 32
	mask = 32 - sub
	no_of_avail_ip_addr= pow(2, mask)
	host_ip_address = no_of_avail_ip_addr - 2
	return no_of_avail_ip_addr,host_ip_address

def reset():
	ip.set('')
	subnet.set(0)
	netw.set('')
	broad.set('')
	avail_host.set('')
	rang.set('')
	

def calc():
	ip_addr = [int(x) for x in ip.get().split(".")]
	sub = subnet.get()
	network_addr = net_addr(ip_addr,sub)
	lst = []
	lst1 = []
	for i in network_addr:
		lst.append(str(i))
	netw.set(".".join(lst))
	broadcast_addr = broad_addr(ip_addr,sub)
	for i in broadcast_addr:
		lst1.append(str(i))
	broad.set(".".join(lst1))
	no_avail,host_ip = available_host(ip_addr,sub)
	avail_host.set(f"Available: {no_avail} Actual avail: {host_ip}")
	network_addr[3] = int(network_addr[3]) + 1
	start_range = ".".join(map(str, network_addr))
	broadcast_addr[3] = int(broadcast_addr[3]) - 1
	end_range = ".".join(map(str, broadcast_addr))
	rang.set(f"{start_range} '-' {end_range}")



tk.Label(win,text = "IP Address").grid(row=0,column=0)
ipfield = tk.Entry(win,textvariable=ip)
ipfield.grid(row=0,column=1)

tk.Label(win, text="Subnet").grid(row=1, column=0)
subnetfield = tk.Entry(win, textvariable=subnet)
subnetfield.grid(row=1, column=1)


tk.Button(win,text="Calculate",command = calc).grid(row=3,column=0)
tk.Button(win,text="Reset",command = reset).grid(row=3,column=1)

tk.Label(win,text = "Network Address").grid(row=5,column=0)
netwfield = tk.Entry(win,textvariable=netw)
netwfield.grid(row=5,column=1)

tk.Label(win, text="Broadcast Address").grid(row=6, column=0)
brodfield = tk.Entry(win, textvariable=broad)
brodfield.grid(row=6, column=1)

tk.Label(win,text = "No of Available IP's").grid(row=7,column=0)
avail_hostfield = tk.Entry(win,textvariable=avail_host)
avail_hostfield.grid(row=7,column=1)

tk.Label(win,text = "Range").grid(row=8,column=0)
rangefield = tk.Entry(win,textvariable=rang)
rangefield.grid(row=8,column=1)

win.mainloop()
