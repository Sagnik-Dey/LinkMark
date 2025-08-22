function showToast(message, status, time) {
    if (status === "error") {
        Lobibox.notify("error", {
            msg: `${message}`,
            icon: "fa fa-times-circle",
            sound: false,
            position: "bottom left",
            delay: time
        });
    }
    
    else if (status === "warning") {
        Lobibox.notify("warning", {
            msg: `${message}`,
            icon: "fa fa-exclamation-triangle",
            sound: false,
            position: "bottom left",
            delay: time
        });
    }
    else if (status === "success") {
        Lobibox.notify("success", {
            msg: `${message}`,
            icon: "fa fa-check-circle",
            sound: false,
            position: "bottom left",
            delay: time
        });
    }
    else if (status === "info") {
        Lobibox.notify("info", {
          msg: `${message}`,
          icon: "fa fa-info-circle",
          sound: false,
          position: "bottom left",
          delay: time,
        });
    }
}

if (document.body.id === "register-page") {
    document.addEventListener('DOMContentLoaded', () => {
        if (window.messages.length > 0) {
            const firstMessage = window.messages[0];
            showToast(firstMessage, "error", 3000);
            }    
        });
        
    const password = document.querySelector("#password");
    const registerBtn = document.querySelector("#register-btn");
    registerBtn.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();

        if (password.value.length < 8) {
            console.log("HERE");
            const message = "Stronger passwords start at 8 characters — you’ve got this!!"
            showToast(message, "warning", 2500);
            return;
        }

        document.querySelector("form").submit();
    });
}
else if (document.body.id === "login-page") {
    document.addEventListener("DOMContentLoaded", () => {
        const flashedMsg = window.flashedMessages;
        if (flashedMsg.length > 0) {
            showToast(flashedMsg[0][1], flashedMsg[0][0], 3000);
        }
    });
}
else if (document.body.id === "home-page") {
    document.addEventListener("DOMContentLoaded", () => {
        const flashedMsg = window.flashedMessages;
        if (flashedMsg.length > 0) {
            showToast(flashedMsg[0][1], flashedMsg[0][0], 3000);
        }
        let cardArray = document.getElementsByClassName("card");
        cardArray = Array.from(cardArray);

        cardArray.forEach(element => {
            element.addEventListener("click", (event) => {
                event.stopPropagation();
                event.preventDefault();
                const cardId = element.id;
                window.location.href = `/view?id=${cardId}`
            });
        });

        let deleteBtnArray = document.getElementsByClassName("delete-btn");
        deleteBtnArray = Array.from(deleteBtnArray);

        deleteBtnArray.forEach(element => {
            element.addEventListener("click", (event) => {
                event.stopPropagation();
                event.preventDefault();

                new jBox("Confirm", {
                  content: "Are you sure you want to delete the marked link?",
                  confirmButton: "Delete",
                  cancelButton: "Cancel",
                  confirm: function () {
                    const parent = element.parentElement.parentElement;
                    const cardId = parent.id;
                    window.location.href = `/delete?id=${cardId}`;
                  },
                  cancel: function() {
                    showToast(
                      "All good! The link is still here.",
                      "info",
                      3000
                    );
                  },
                }).open();
            })
        });

        const logoutBtn = document.querySelector("#logout-btn");
        logoutBtn.addEventListener("click", (event) => {
            event.stopPropagation();
            event.preventDefault();

            new jBox("Confirm", {
              content: "Logging out will end your session. Continue?",
              confirmButton: "Logout",
              cancelButton: "Stay",
              confirm: function () {
                window.location.href = "/home/logout";
              },
              cancel: function() {
                showToast("You’re still with us!", "info", 3000);
              },
            }).open();
        });
    });

}
else if (document.body.id === "landing-page") {
    document.addEventListener("DOMContentLoaded", () => {
        const flashedMsg = window.flashedMessages;
        console.log(flashedMsg);
        if (flashedMsg.length > 0) {
            showToast(flashedMsg[0][1], flashedMsg[0][0], 3000);
        }
    });
}