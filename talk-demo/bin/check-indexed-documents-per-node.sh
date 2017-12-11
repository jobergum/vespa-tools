for host in $(vespa-model-inspect -u service searchnode |grep JSON | awk '{print $1}'); do 
	echo -n $host" "
	curl -s $host"state/v1/custom/component/documentdb/tweet" |python -m json.tool |grep indexed
done
