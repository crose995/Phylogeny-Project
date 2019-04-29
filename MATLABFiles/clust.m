dist = pdist(data2,"jaccard");
link = linkage(dist,"single");
dendrogram(link,0,"Labels",labels)