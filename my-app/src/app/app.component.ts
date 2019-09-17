import { Component, OnInit } from "@angular/core";
import {
  NgForm,
  FormGroup,
  ReactiveFormsModule,
  FormBuilder,
  Validators
} from "@angular/forms";
import { HttpClient, HttpHeaders } from "@angular/common/http";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent implements OnInit {
  title = "my-app";
  private commandeForm: FormGroup;
  constructor(private fb: FormBuilder, private httpClient: HttpClient) {}
  public onSubmit() {
    let httpHeaders = new HttpHeaders({
      "Content-Type": "application/json",
      "Cache-Control": "no-cache"
    });

    let options = {
      headers: httpHeaders
    };
    let maCommande = {
      nom: this.commandeForm.value.nom,
      adresse: this.commandeForm.value.adresse
    };
    this.httpClient
      .post("http://127.0.0.1:5000/commandes", maCommande, options)
      .subscribe(
        val => {
          console.log("POST call successful value returned in body", val);
        },
        response => {
          console.log("POST call in error", response);
        },
        () => {
          console.log("The POST observable is now completed.");
        }
      );
  }
  FormGroup(arg0: { id: any }, adresse: any, arg2: string) {
    throw new Error("Method not implemented.");
  }
  ngOnInit() {
    this.commandeForm = this.fb.group({
      nom: ["", Validators.required],
      adresse: ["", Validators.required]
    });
  }
}
