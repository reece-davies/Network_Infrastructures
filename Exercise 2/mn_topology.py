




def emulate(depth_, fanout_):
    
    # Create a network with tree topology
    tree_ = TreeTopo(depth=depth_,fanout=fanout_)
    
    # Initiating the Mininet instance
    net = Mininet(topo=tree_)
    
    # Start Execution of the Emulated System.
    net.start()

    # Name two of the instances as h1 and h2.
    h1, h2  = net.hosts[0], net.hosts[depth_]

    # Ping from an instance to another, and print the output.
    print (h1.cmd('ping -c1 %s' % h2.IP()))

    # Stop the Mininet Emulation.
    net.stop()





