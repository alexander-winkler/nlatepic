let counter = document.querySelector("#counter");
            let table = document.querySelector("#database"), row, authCell, titlCell, noboCell, noveCell;

            fetch('works.json')
                .then(response => response.json())
                .then(data => {
                    counter.innerHTML = data.length;
                    
                    for (var i = 0; len = data.length; i++) {
                        
                        let obj = data[i];

                        
                        row = document.createElement("tr");
                        authCell = document.createElement("td");
                        titlCell = document.createElement("td");
                        noboCell = document.createElement("td");
                        noveCell = document.createElement("td");
                        subjCell = document.createElement("td");
                        digiCell = document.createElement("td");

                        if (typeof obj.author.name != "undefined") {
                            console.log(obj.author.name)
                            authCellText = obj.author.name
                        } else {
                            authCellText = "Anoynmus/Unknown";
                        }
                        
                        if (typeof obj.author.ID != "undefined") {
                            obj.author.ID.forEach(entry => {
                            Object.keys(entry).forEach(KEY => {
                                
                                if (KEY === "wikidata") {
                                    console.log(`https://www.wikidata.org/wiki/${entry[KEY]}`) ;
                                    authCellText += ` <a href="https://www.wikidata.org/wiki/${entry[KEY]}"><img src="img/WKP.png"></img></a>`
                                }

                                if (KEY === "GND") {
                                    console.log(`${entry[KEY]}`) ;
                                    authCellText += ` <a href="${entry[KEY]}"><img src="img/DNB.png"></img></a>`
                                }

                                if (KEY === "VIAF") {
                                    console.log(`${entry[KEY]}`) ;
                                    authCellText += ` <a href="${entry[KEY]}"><img src="img/Viaf_icon.png"></img></a>`
                                }

                                if (KEY === "BNF") {
                                    console.log(`${entry[KEY]}`) ;
                                    authCellText += ` <a href="https://catalogue.bnf.fr/${entry[KEY]}"><img src="img/Logo_BNF_Web.png"></img></a>`
                                }
                            })})
                        }

                        if (typeof obj.content.subject != "undefined") {
                            let subjCellText = "";
                            obj.content.subject.forEach(entry => {
                                if (typeof entry.label === "undefined") {
                                    var label = " << to be added >>";
                                } else {
                                    var label = entry.label.value;
                                }
                                subjCellText += `<a href="https://www.wikidata.org/wiki/${entry.url}">${label} <img src="img/WKP.png"></img></a>`
                            })
                            subjCell.innerHTML = subjCellText;
                        }

                        
                        authCell.innerHTML = authCellText;
                        titlCell.innerHTML = obj.title;


                        if (typeof obj.content.num_books != "undefined") {
                            noboCell.innerHTML = obj.content.num_books;
                        } else {
                            noboCell.innerHTML = "-";
                        }

                        if (typeof obj.content.num_verses != "undefined") {
                            noveCell.innerHTML = obj.content.num_verses;
                        } else {
                            noveCell.innerHTML = "-";
                        }

                        if (typeof obj.urls != "undefined") {
                            let digiCellText = "";
                            obj.urls.forEach(url => {
                                digiCellText += `<a href="${url}"><img src="img/Book.png"></img></a>`;
                            digiCell.innerHTML = digiCellText;
                            })};
                        

                        table.appendChild(row);
                        row.appendChild(authCell);
                        row.appendChild(titlCell);
                        row.appendChild(noboCell);
                        row.appendChild(noveCell);
                        row.appendChild(subjCell);
                        row.appendChild(digiCell);

                            
                 } });  