package com.internship.tool.controller;

import com.internship.tool.dto.ComplianceDTO;
import com.internship.tool.entity.Compliance;
import com.internship.tool.service.ComplianceService;

import jakarta.validation.Valid;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/compliance")
public class ComplianceController {

    private final ComplianceService service;

    public ComplianceController(ComplianceService service) {
        this.service = service;
    }

    
    private Compliance mapToEntity(ComplianceDTO dto) {
        Compliance c = new Compliance();
        c.setTitle(dto.getTitle());
        c.setDescription(dto.getDescription());
        c.setCategory(dto.getCategory());
        c.setStatus(dto.getStatus());
        c.setRiskScore(dto.getRiskScore());
        return c;
    }

   
    @GetMapping("/all")
    public ResponseEntity<Page<Compliance>> getAll(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "5") int size
    ) {
        Page<Compliance> data = service.getAllPaginated(PageRequest.of(page, size));
        return ResponseEntity.ok(data);
    }

    
    @GetMapping("/{id}")
    public ResponseEntity<Compliance> getById(@PathVariable Long id) {
        return ResponseEntity.ok(service.getComplianceById(id));
    }

    
    @PostMapping("/create")
    public ResponseEntity<Compliance> create(@Valid @RequestBody ComplianceDTO dto) {
        Compliance saved = service.createCompliance(mapToEntity(dto));
        return new ResponseEntity<>(saved, HttpStatus.CREATED);
    }

    // ✅ UPDATE
    @PutMapping("/{id}")
    public ResponseEntity<Compliance> update(
            @PathVariable Long id,
            @Valid @RequestBody ComplianceDTO dto
    ) {
        Compliance updated = service.updateCompliance(id, mapToEntity(dto));
        return ResponseEntity.ok(updated);
    }

    // ✅ DELETE
    @DeleteMapping("/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id) {
        service.deleteCompliance(id);
        return ResponseEntity.ok("Deleted successfully");
    }
}