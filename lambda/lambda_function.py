if(ans.value === "correct"){
score++;
}
});

const data = {
name: document.getElementById("name").value,
email: document.getElementById("email").value,
phone: document.getElementById("phone").value,
score: score,
attempted: attempted
};

fetch("https://bslhqdr87i.execute-api.ap-south-1.amazonaws.com/prod/submit",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

})
.then(response => response.json())
.then(result => {

alert("Quiz submitted successfully! Score: " + score);

})
.catch(error => {

alert("Error submitting quiz");

});

}

</script>

</body>
</html>
