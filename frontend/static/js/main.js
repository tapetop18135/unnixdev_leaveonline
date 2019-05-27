const main_url = "http://127.0.0.1:3200"
$(document).ready(function(){
    $(".policy").on("click", function(e){
        deletecontent("policy")
        console.log(`${main_url}/api/get_policys`)

        fetch(`${main_url}/api/get_policys`)
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                data = data["policys"]
                var div_policy = ""
                console.log(data)
                for(i in data){
                    debugger
                    div_policy += `
                    <div>
                        <p>
                            <span class="poliName_${data[i][0][2]}">${data[i][0][1]}</span> 
                            <span class="poliDep_${data[i][1][2]}">${data[i][1][1]}</span> 
                            <span class="poliPos_${data[i][2][2]}">${data[i][2][1]}</span> 
                            <span class="poliNum_${data[i][3][2]}">${data[i][3][1]}</span>
                        </p>
                    </div>
                    `
                }
                $(".con_policy").html(`<h1>POLICY</h1>${div_policy}`)
            });


    })
    $(".approvepaper").on("click", function(e){
        
        var username = $("#username_").text()
        deletecontent("approvepaper")
        var staffID = username
        var iframe = `https://docs.google.com/forms/d/e/1FAIpQLSfQYEmVaeE3gCTDyyfkzhEPIR2lZrFqXvAQ4ISyWmQBkmrUdw/viewform?embedded=true&entry.1829276584=${staffID}`
        
        divC = `<div class="test1 googleS" style=
            "top: 40px;
            z-index : 1;
            position : absolute;
            left: 50%;
            transform: translate(-50%,0);">

            <iframe src=${iframe} width="640" height="1105" frameborder="0" marginheight="0" marginwidth="0">กำลังโหลด...</iframe>
        </div>`

        $(".con_approvepaper").html(`${divC}`)
        $(".googleS").show()
    })
    $(".status").on("click", function(e){
        
        deletecontent("status")
        $(".con_status").html("<h1>STATUS</h1>")
    })
    $(".supermode").on("click", function(e){
        
        deletecontent("supermode")  
        $(".con_supermode").html("<h1>SUPERVISOR</h1>")
    })
    

    $(document).ready(function(){
        $(".balckground_opa").on("click", ()=>{
            console.log("ssssss")
            $(".googleS").hide()
        })
    })

})

function getKey(obj){
    debugger
    for( i in obj){
        return i
    }
}

function deletecontent(now){
    var arr = ["policy", "approvepaper", "status", "supermode"]
    for(val of arr){
        if(val == now) continue;
        $(`.con_${val}`).empty()
    }
}