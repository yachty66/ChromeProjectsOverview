//go to https://www.maxhager.xyz/ and get every tag between first h2 tags 
function getTags() {
    //get DOM from https://www.maxhager.xyz/


    var tags = [];
    var h2 = document.getElementsByTagName('h2');
    var h2tags = h2[0].getElementsByTagName('a');
    for (var i = 0; i < h2tags.length; i++) {
        tags.push(h2tags[i].innerHTML);
    }
    return tags;
}
//create in the middle of index.html a table and add every tag to this table
//execute js file every minute 
//seems to be not so easy to get dom with js
//i will just all headlines with python and put them into a text file 
//i read this text file and put every headline into a table with js 
//in the end i can do everything with python. i also can directly put the headlines into a table with python

console.log(getTags());