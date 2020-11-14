#!/bin/bash
	source /root/.bash_profile

	vip=`echo '192.168.1.59/24'`  #设置VIP
	key=`echo '1'`

	command=`echo "$1" | awk -F = '{print $2}'`
	orig_master_host=`echo "$2" | awk -F = '{print $2}'`
	new_master_host=`echo "$7" | awk -F = '{print $2}'`
	orig_master_ssh_user=`echo "${12}" | awk -F = '{print $2}'`
	new_master_ssh_user=`echo "${13}" | awk -F = '{print $2}'`

	#要求服务的网卡识别名一样，都为ens192(这里是)
	stop_vip=`echo "ssh root@$orig_master_host /usr/sbin/ifconfig ens192:$key down"`
	start_vip=`echo "ssh root@$new_master_host /usr/sbin/ifconfig ens192:$key $vip"`

	if [ $command = 'stop' ]
	  then
	    echo -e "\n\n\n****************************\n"
	    echo -e "Disabled thi VIP - $vip on old master: $orig_master_host \n"
	    $stop_vip
	    if [ $? -eq 0 ]
	      then
		echo "Disabled the VIP successfully"
	      else
		echo "Disabled the VIP failed"
	    fi
	    echo -e "***************************\n\n\n"
	  fi

	if [ $command = 'start' -o $command = 'status' ]
	  then
	    echo -e "\n\n\n*************************\n"
	    echo -e "Enabling the VIP - $vip on new master: $new_master_host \n"
	    $start_vip
	    if [ $? -eq 0 ]
	      then
		echo "Enabled the VIP successfully"
	      else
		echo "Enabled the VIP failed"
	    fi
	    echo -e "***************************\n\n\n"
	fi