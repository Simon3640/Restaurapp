import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { CategoryService } from '@app/shared/services/category.service';


@Component({
  selector: 'app-new-product',
  templateUrl: './new-product.component.html',
  styleUrls: ['./new-product.component.scss']
})
export class NewProductComponent implements OnInit {

  constructor(private fb: FormBuilder) { }

  productForm = this.fb.group({
    Name: ['',[Validators.required, Validators.minLength(3), Validators.maxLength(255)]],
    Description: ['',[Validators.required, Validators.minLength(20), Validators.maxLength(300)]],
    Short_Description: ['',[ Validators.minLength(0), Validators.maxLength(100)]],
    Value: [Number, [Validators.required, Validators.min(0), Validators.max(100000000000)]],
  });

  ngOnInit(): void {
  }
  Entero(Value: number): boolean {
    return Number.isInteger(Value);
  }

  isInvalidForm(controlName: string): boolean {
    return this.productForm.controls[controlName].invalid && this.productForm.controls[controlName].touched;}

}
