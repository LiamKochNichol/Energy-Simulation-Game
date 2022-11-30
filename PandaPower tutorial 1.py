import pandapower as pp
def Tutorial1_PF(x,y):
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
  pp.create_sgen(net, bus=b1,p_mw=x) #set as gen_set[0]
  pp.create_sgen(net, bus=b2,p_mw=y) #set as gen_set[1]
  pp.runpp(net)
  print(net.res_bus.vm_pu)
  print(net.res_ext_grid)
  print(net.res_line)
  return [net.res_ext_grid,net.res_line]