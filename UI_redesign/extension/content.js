
console.log("Running on Google only because of manifest.json");

var gh_img_src = "https://cdn.ndtv.com/static/ndtv_2014/images/ndtvlogo_blk.png?1";

function getData(url, callback) {
    $.get('https://allorigins.me/get?method=raw&url=' + encodeURIComponent(url) + '&callback=?', function(data) {
        console.log(data);
        callback(data);
    });
}


function xpath(xpath_string, dom) {
    var result = [];
    var nodes_snapshot = document.evaluate(xpath_string, dom, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
    for (var i = 0; i < nodes_snapshot.snapshotLength; i++) {
        result.push(nodes_snapshot.snapshotItem(i));
    }
    return result;
}

console.log("abcd");

function createElementFromHTML(htmlString) {
    var div = document.createElement('div');
    div.innerHTML = htmlString.trim();
    return div.firstChild;
}

function searchGH_SO() {
    console.log("within searchGH_SO");

    var gh_url = "https://www.ndtv.com/latest/page-1";
    getData(gh_url, function(data) {
      
        filterGithub(data);
    });
}

function filterGithub(data) {
    var dom = createElementFromHTML(data);
    var list_titles = xpath("//div[contains(@class,'nstory_header')]", dom);
    var list_desc = xpath("//div[contains(@class,'nstory_intro')]", dom);
   
   
    //f.open("w"); // open file with write access
    //for (var i = 0; i < list_titles.length; i++) {
    document.getElementById("x").innerHTML="myunsvs"; 
} 



searchGH_SO();



console.log("Finished Running");