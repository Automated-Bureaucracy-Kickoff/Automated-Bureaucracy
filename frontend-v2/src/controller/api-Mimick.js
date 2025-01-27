// i am mimicking api , as api has not been created ,so i created a js fnction which behaves like this

let count = 0 
function mimickApi(message){
  
    return new Promise((res,rej)=>{
         setTimeout(()=>{
            if(count==0){
                res(JSON.stringify({message:`${message} i am mimicking an api `}))
                count+=1
              }else{
                rej(JSON.stringify({message:`We apologize for the issue. It's not a problem with your request, but rather a technical difficulty on our end.`}))
                count=0
              }
         },200)
       
    })
}


export default mimickApi