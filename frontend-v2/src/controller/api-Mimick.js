// i am mimicking api , as api has not been created ,so i created a js fnction which behaves like this

let count = 0 
function mimickApi(message){
   console.log("USER MESSAGE",message)
    return new Promise((res,rej)=>{
         setTimeout(()=>{
            if(count==0){
                res(JSON.stringify({message:`${message.message}  THESE are the settings ${message.settings} i am mimicking an api and here is the setting `}))
                count+=1
              }else{
                rej(JSON.stringify({message:`  Hmm something went wrong  `}))
                count=0
              }
         },2000)
       
    })
}


export default mimickApi