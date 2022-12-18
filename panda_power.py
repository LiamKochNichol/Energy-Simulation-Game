import pandapower as pp
import warnings
warnings.filterwarnings("ignore")

def PF_tut1(gen_outputs):
    line_out = []
    net = pp.create_empty_network()
    line={
    "x_ohm_per_km": 0.1,
    "r_ohm_per_km": 0,
    "c_nf_per_km": 0,
    "max_i_ka": 1}
    pp.create_std_type(net,data=line,name='blah')
    b1 = pp.create_bus(net,vn_kv=200.)
    b2 = pp.create_bus(net,vn_kv=200.)
    b3 = pp.create_bus(net,vn_kv=200.)
    pp.create_line(net,from_bus=b1,to_bus=b2,length_km=5, std_type="blah")
    pp.create_line(net,from_bus=b2,to_bus=b3,length_km=15, std_type="blah")
    pp.create_line(net,from_bus=b1,to_bus=b3,length_km=10, std_type="blah")
    pp.create_ext_grid(net, bus=b3)
    pp.create_sgen(net, bus=b1,p_mw=gen_outputs[0])  #set as gen_set[0]
    pp.create_sgen(net, bus=b2,p_mw=gen_outputs[1])  #set as gen_set[1]
    pp.rundcpp(net)
    #print(net.res_bus.vm_pu)
    #print(net.res_ext_grid)
    #print(net.res_line)
    for i in range(0, len(net.res_line.index)):
        line_out = line_out + [net.res_line.at[i, "p_from_mw"]]
        #print(net.res_line.at[i, "p_from_mw"])

    return line_out

def PF_tut3(gen_outputs,load_value):
    line_out = []
    line_out_loading=[]
    net = pp.create_empty_network()
    line={
    "x_ohm_per_km": 0.1,
    "r_ohm_per_km": 0.5,
    "c_nf_per_km": 0,
    "max_i_ka": 0.25}
    pp.create_std_type(net,data=line,name='blah')
    b1 = pp.create_bus(net,vn_kv=200.)
    b2 = pp.create_bus(net,vn_kv=200.)
    b3 = pp.create_bus(net,vn_kv=200.)
    pp.create_line(net,from_bus=b1,to_bus=b2,length_km=5, std_type="blah")
    pp.create_line(net,from_bus=b2,to_bus=b3,length_km=15, std_type="blah")
    pp.create_line(net,from_bus=b1,to_bus=b3,length_km=10, std_type="blah")
    pp.create_ext_grid(net, bus=b3)
    pp.create_sgen(net, bus=b1,p_mw=gen_outputs[0])  #set as gen_set[0]
    pp.create_sgen(net, bus=b2,p_mw=gen_outputs[1])  #set as gen_set[1]
    pp.rundcpp(net)
    #print(net.res_bus.vm_pu)
    #print(net.res_ext_grid)
    #print(net.res_line)
    for i in range(0, len(net.res_line.index)):
        line_out=line_out+[net.res_line.at[i,"p_from_mw"]]
        line_out_loading = line_out_loading + [net.res_line.at[i, "loading_percent"]]
        #print(net.res_line.at[i, "p_from_mw"])
    power_imbalance=load_value+net.res_ext_grid.at[0,"p_mw"]
    return [line_out,line_out_loading, power_imbalance]

def PF_tut3_loss(gen_outputs):
    line_out = []
    line_out_loading=[]
    net = pp.create_empty_network()
    line={
    "x_ohm_per_km": 0.1,
    "r_ohm_per_km": 0.5,
    "c_nf_per_km": 0,
    "max_i_ka": 0.25}
    pp.create_std_type(net,data=line,name='blah')
    b1 = pp.create_bus(net,vn_kv=200.)
    b2 = pp.create_bus(net,vn_kv=200.)
    b3 = pp.create_bus(net,vn_kv=200.)
    pp.create_line(net,from_bus=b1,to_bus=b2,length_km=5, std_type="blah")
    pp.create_line(net,from_bus=b2,to_bus=b3,length_km=15, std_type="blah")
    pp.create_line(net,from_bus=b1,to_bus=b3,length_km=10, std_type="blah")
    pp.create_ext_grid(net, bus=b1)
    pp.create_sgen(net, bus=b2,p_mw=gen_outputs[0])  #set as gen_set[0]
    pp.create_load(net,bus=b3,p_mw=150)
    pp.runpp(net)
    #print(net.res_bus.vm_pu)
    #print(net.res_ext_grid)
    #print(net.res_line)
    for i in range(0, len(net.res_line.index)):
        line_out=line_out+[net.res_line.at[i,"p_from_mw"]]
        line_out_loading = line_out_loading + [net.res_line.at[i, "loading_percent"]]
        #print(net.res_line.at[i, "p_from_mw"])
        #400 X_base
    return [line_out, line_out_loading, round(net.res_ext_grid.at[0, "p_mw"], 1)]





