function cs = cosine_similarity(typeid1,typeid2,NumberPeople)


np_matrix = NumberPeople.Variables;
t1_time = np_matrix(typeid1,2:width(np_matrix));
t2_time = np_matrix(typeid2,2:width(np_matrix));

cs = dot(t1_time,t2_time)/(norm(t1_time)*norm(t2_time));


end

